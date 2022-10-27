const setup = () => {
    $.ajaxSetup({
        headers: {"X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()}
    });
    fixHistoryTable();
}

const fixHistoryTable = () => {
    $.getJSON("json", function (data) {
        $.each(data, function (key, item) {
            $("#history-table").append(
                `<tr>
                    <td>${item.fields.date_time}</td>
                    <td>${item.fields.type}</td>
                    <td>${item.fields.mass}</td>
                </tr>`
            );
        });
    });
}