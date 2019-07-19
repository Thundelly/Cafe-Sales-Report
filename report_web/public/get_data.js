function getFromDatabase() {

    const firebaseConfig = {
        apiKey: "AIzaSyBKvJsQ_p38KWY8xSZANHL2BbaVCLPcGNw",
        authDomain: "salesinfo-spaceeum.firebaseapp.com",
        databaseURL: "https://salesinfo-spaceeum.firebaseio.com",
        projectId: "salesinfo-spaceeum",
        storageBucket: "salesinfo-spaceeum.appspot.com",
        messagingSenderId: "649465922023",
        appId: "1:649465922023:web:60970cc6ba586487"
    };

    // Initialize Cloud Firestore through Firebase

    if (!firebase.apps.length) {
        firebase.initializeApp(firebaseConfig);
    }

    let date;
    let year;
    let month;
    let day;

    date = new Date();
    year = String(date.getFullYear());
    month = ('0' + String(date.getMonth() + 1)).slice(-2);
    day = ('0' + String(date.getDate())).slice(-2);

    var db = firebase.firestore();

    docRef = db.collection("Space.EUm").doc("Sales Data").collection(year).doc(month).collection(day);
    docRef
        .get()
        .then(qs => {
            qs.forEach(doc => {
                if (doc.id === "system") {
                    document.getElementById('name').innerHTML = doc.data()['Name'].bold();
                    document.getElementById('date').innerHTML = doc.data()['Date'].bold();
                    document.getElementById('cash_sale').innerHTML = doc.data()['Cash Sale'];
                    document.getElementById('card_sale').innerHTML = doc.data()['Card Sale'];
                    document.getElementById('total_fees').innerHTML = doc.data()['Total Fees'];
                    document.getElementById('total_refunds').innerHTML = doc.data()['Total Refunds'];
                    document.getElementById('net_sale').innerHTML = doc.data()['Net Sale'];
                    document.getElementById('card_tip').innerHTML = doc.data()['Card Tip'];
                    document.getElementById('cash_in_drawer').innerHTML = doc.data()['Cash in drawer'];
                    if ((doc.data()['Cash Discrepancy']).slice(1, doc.data()['Cash Discrepancy'].length) < 0){
                        document.getElementById('discrepancy').innerHTML = doc.data()['Cash Discrepancy'].fontcolor("red");
                    } else {
                        document.getElementById('discrepancy').innerHTML = doc.data()['Cash Discrepancy'].fontcolor("green");
                    }

                }
                else if (doc.id === "drawer"){
                    if (doc.data()['hundred'] !== ""){
                        document.getElementById('hundred').innerHTML = doc
                            .data()['hundred'].bold() + ': $' + (parseInt(doc.data()['hundred']) * 100).toFixed(2);
                    }
                    else {
                        document.getElementById('hundred').innerHTML = 0;
                    }

                    if (doc.data()['fifty'] !== ""){
                        document.getElementById('fifty').innerHTML = doc
                            .data()['fifty'].bold() + ': $' + (parseInt(doc.data()['fifty']) * 50).toFixed(2);
                    }
                    else {
                        document.getElementById('fifty').innerHTML = 0;
                    }

                    if (doc.data()['twenty'] !== ""){
                        document.getElementById('twenty').innerHTML = doc
                            .data()['twenty'].bold() + ': $' + (parseInt(doc.data()['twenty']) * 20).toFixed(2);
                    }
                    else {
                        document.getElementById('twenty').innerHTML = 0;
                    }

                    if (doc.data()['ten'] !== ""){
                        document.getElementById('ten').innerHTML = doc
                            .data()['ten'].bold() + ': $' + (parseInt(doc.data()['ten']) * 10).toFixed(2);
                    }
                    else {
                        document.getElementById('ten').innerHTML = 0;
                    }

                    if (doc.data()['five'] !== ""){
                        document.getElementById('five').innerHTML = doc
                            .data()['five'].bold() + ': $' + (parseInt(doc.data()['five']) * 5).toFixed(2);
                    }
                    else {
                        document.getElementById('five').innerHTML = 0;
                    }

                    if (doc.data()['one'] !== ""){
                        document.getElementById('one').innerHTML = doc
                            .data()['one'].bold() + ': $' + (parseInt(doc.data()['one'])).toFixed(2);
                    }
                    else {
                        document.getElementById('one').innerHTML = 0;
                    }

                    if (doc.data()['quarter'] !== ""){
                        document.getElementById('quarter').innerHTML = doc
                            .data()['quarter'].bold() + ': $' + (parseInt(doc.data()['quarter']) * 0.25).toFixed(2);
                    }
                    else {
                        document.getElementById('quarter').innerHTML = 0;
                    }

                    if (doc.data()['dime'] !== ""){
                        document.getElementById('dime').innerHTML = doc
                            .data()['dime'].bold() + ': $' + (parseInt(doc.data()['dime']) * 0.10).toFixed(2);
                    }
                    else {
                        document.getElementById('dime').innerHTML = 0;
                    }

                    if (doc.data()['nickel'] !== ""){
                        document.getElementById('nickel').innerHTML = doc
                            .data()['nickel'].bold() + ': $' + (parseInt(doc.data()['nickel']) * 0.05).toFixed(2);
                    }
                    else {
                        document.getElementById('nickel').innerHTML = 0;
                    }

                    if (doc.data()['cent'] !== "") {
                        document.getElementById('cent').innerHTML = doc
                            .data()['cent'].bold() + ': $' + (parseInt(doc.data()['cent']) * 0.01).toFixed(2);
                    }
                    else{
                        document.getElementById('cent').innerHTML = 0;
                    }

                    if (doc.data()['roll'] !== ""){
                        document.getElementById('roll').innerText = '$' + parseInt(doc.data()['roll']).toFixed(2);
                    }
                    else {
                        document.getElementById('roll').innerHTML = 0;
                    }
                }
            })
        });
}

window.onload = getFromDatabase();
