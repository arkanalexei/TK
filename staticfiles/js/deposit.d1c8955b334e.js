function setup() {
    alert("setup"); 
    $.ajaxSetup({
        headers: {"X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()}
    });
    
    $(`#submitBtn`).on('click', updateHistoryTable(`#submitForm`));
}

const appendHistoryTable = () => {
    $.getJSON("json", function (data) {
        for (var i = data.length - 1; (i >= 0) && (data.length - i <= 5); i--) {
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

const updateHistoryTable = (form) => {
    console.log("what");
    $.post(
        `submit/`, $(form).serialize(), (data) => 
    );
    $(`#history-table`).empty();
    appendHistoryTable();
}