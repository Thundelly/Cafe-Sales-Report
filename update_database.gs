function onFormSubmit() {

// ACCESS GOOGLE FORMS AND RETRIEVE INPUT DATA. ID: 1P6rQz5iJJENIj27lqjPJV_PnW-65xoFG15j2vrhs-6Y
  var form = FormApp.openById("1P6rQz5iJJENIj27lqjPJV_PnW-65xoFG15j2vrhs-6Y");
  var formResponses = form.getResponses();

  for (var i = 0; i < formResponses.length; i++) {
  var formResponse = formResponses[i];
  var itemResponses = formResponse.getItemResponses();
  for (var j = 0; j < itemResponses.length; j++) {
    var itemResponse = itemResponses[j];

    if (j === 0){
    var name = itemResponse.getResponse()
    } else if (j === 1){
    var hundred = itemResponse.getResponse()
    } else if (j === 2){
    var fifty = itemResponse.getResponse()
    } else if (j === 3){
    var twenty = itemResponse.getResponse()
    } else if (j ===4){
    var ten = itemResponse.getResponse()
    } else if (j === 5){
    var five = itemResponse.getResponse()
    } else if (j === 6){
    var one = itemResponse.getResponse()
    } else if (j === 7){
    var quarter = itemResponse.getResponse()
    } else if (j === 8){
    var dime = itemResponse.getResponse()
    } else if (j === 9){
    var nickel = itemResponse.getResponse()
    } else if (j === 10){
    var cent = itemResponse.getResponse()
    } else if (j === 11){
    var roll = itemResponse.getResponse()
    }
  }
 }
 
// CLEAR GOOGLE FORMS DATA
    form.deleteAllResponses();

// FIND CURRENT TIME IN PDT
  var date = Utilities.formatDate(new Date(), "GMT-7", "yyyy-MM-dd");

// MAKE HTTPS REQUEST TO GOOGLE CLOUD PLATFORM
  var url = "https://us-central1-spaceeum.cloudfunctions.net/CafeClosing?name=" + name + "&date=" + date + 
  "&hundred=" + hundred + "&fifty=" + fifty + "&twenty=" + twenty + "&ten=" + ten + "&five=" + five + "&one=" + one + "&quarter=" + quarter
  + "&dime=" + dime + "&nickel=" + nickel + "&cent=" + cent + "&roll=" + roll

  var response = UrlFetchApp.fetch(url);
}