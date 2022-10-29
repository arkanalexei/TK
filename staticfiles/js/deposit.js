// Initial setup
function setup() {
    $.ajaxSetup({ // set up CSRF token for all HTTP requests
        headers: {"X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()}
    });
    updateHistoryTable();
    updatePointCount();
}

<<<<<<< HEAD
=======
// Show 5 of the most recent deposits under #history-table
>>>>>>> 85a52418f61eaf082ddb9193e18aeb808d650d37
function updateHistoryTable() {
    $(`#history-table`).empty();    // empty table before appending html
    $.getJSON("json/", (data) => {  // retrieve user's data
        const len = data.length;
        for (var i = len - 1; (i >= 0) && (len - i <= 5); i--) {
            // append row of WasteDeposit data
            $("#history-table").append(
                `<tr>
                <td>${data[i].fields.date_time}</td>
                <td>${data[i].fields.type}</td>
                <td>${data[i].fields.mass}</td>
                <td>${data[i].fields.description}</td>
                </tr>`
            );
        }
    });
}

<<<<<<< HEAD
=======
// Show user's point count in .point-count
>>>>>>> 85a52418f61eaf082ddb9193e18aeb808d650d37
function updatePointCount() {
    $.getJSON(
        "json/achiever/", (data) => {
            $(`.point-count`).empty();
            $(`.point-count`).append(data[0].fields.points);
        }
    );
}

<<<<<<< HEAD
=======
// Create an AJAX post request when deposit form is submitted
>>>>>>> 85a52418f61eaf082ddb9193e18aeb808d650d37
function submitDeposit(form) {
    $.post(
        `submit/`, $(form).serialize(), () => {
            updateHistoryTable();
            updatePointCount();
<<<<<<< HEAD
            $("#depositForm")[0].reset();   // reset form fields
=======
            $("#depositForm")[0].reset(); // reset form fields
            $(".modal").hide();
>>>>>>> 85a52418f61eaf082ddb9193e18aeb808d650d37
        }
    );
}