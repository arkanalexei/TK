const setup = () => {
    $.ajaxSetup({
        headers: {"X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()}
    });
    fixHistoryTable();
}

const fixHistoryTable = () => {
    var depositData = $.getJSON("json", (depositData) => {
        alert("success");
        return depositData});

    $.each(depositData, (item) => {
        $("#history-table").append(
            `<tr>
                <td>${item}</td>
                <td>${item.type}</td>
                <td>${item.mass}1more</td>
            </tr>`
        );
    });
}