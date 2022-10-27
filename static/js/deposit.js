function setup() {
    $.ajaxSetup({
        headers: {"X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()}
    });

    appendHistoryTable();
}

function appendHistoryTable() {
    $(`#history-table`).empty();
    $("#depositForm")[0].reset();
    $.getJSON("json/", (data) => {
        const len = data.length;
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
    $.post(
        `submit/`, $(form).serialize(), () => appendHistoryTable()
    );
}