from calculate import Calculate


def main(request):

    drawer = parse_request(request)

    try:
        calculate = Calculate(drawer)
        output = calculate.display()
        calculate.write_to_database(output)

        return str(output)

    except AttributeError as e:
        return "Drawer information not in system. Error: {}".format(e)

def parse_request(request):
    name = request.args.get('name')
    date = request.args.get('date')
    hundred = request.args.get('hundred')
    fifty = request.args.get('fifty')
    twenty = request.args.get('twenty')
    ten = request.args.get('ten')
    five = request.args.get('five')
    one = request.args.get('one')
    quarter = request.args.get('quarter')
    dime = request.args.get('dime')
    nickel = request.args.get('nickel')
    cent = request.args.get('cent')
    roll = request.args.get('roll')

    drawer = {
        'name': name,
        'date': date,
        'hundred': hundred,
        'fifty': fifty,
        'twenty': twenty,
        'ten': ten,
        'five': five,
        'one': one,
        'quarter': quarter,
        'dime': dime,
        'nickel': nickel,
        'cent': cent,
        'roll': roll
    }

    return drawer
