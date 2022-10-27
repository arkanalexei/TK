function setup() {
    $.ajaxSetup({ // set up CSRF token for all HTTP requests
        headers: {"X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()}
    });
    appendHistoryTable();
}

function appendHistoryTable() {
    $(`#history-table`).empty();    // empty table before appending html
    $("#depositForm")[0].reset();   // reset form fields
    $.getJSON("json/", (data) => {  // retrieve user's data
        const len = data.length;
        // append row of WasteDeposit data for 5 of the most recent deposits
        for (var i = len - 1; (i >= 0) && (len - i <= 5); i--) {
            $("#history-table").append(
                `<tr>
                <td>${data[i].fields.date_time}</td>
                <td>${data[i].fields.type}</td>
                <td>${data[i].fields.mass}</td>
                </tr>`
            );
        }
    });
}

function submitDeposit(form) {
    // Create a POST http request to be handled by Django
    $.post(
        `submit/`, $(form).serialize(), () => appendHistoryTable()
    );
}