// TODO: setup
<<<<<<< HEAD
// TODO: function to get the leaderboard data from the server
// TODO: function to display the leaderboard data on the page
// TODO: function to update the leaderboard data on the page
// TODO: function to get the form from the server, and display it on the json page
=======
function setup() {
  $.ajaxSetup({
    // set up CSRF token for all HTTP requests
    headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
  });
  updateLeaderboard();
  // updatePointCount();
}

function updateLeaderboard() {
  $(`#leaderboard-table`).empty(); // empty table before appending html
  $.getJSON("json/", (data) => {
    // retrieve user's data
    const len = data.length;
    // append row of achiever for top 10 achievers
    for (var i = 0; i < len && i < 10; i++) {
      $("#leaderboard-table").append(
        `<tr>
                <td>${i + 1}</td>
                <td>lalalalala</td>
                <td>${data[i].fields.points}</td>
                </tr>`
      );
    }
  });
}

// function submitComment(form) {
//     // Create a POST http request to be handled by Django

//     $.ajax({
//         url: '',
//         type: 'POST',
//         data: {
//             comment : $(comment_text).val(),
//         },
//         success : function(response) {
//             alert("Comment posted successfully");
//         }
//     })

//     $.post(
//         `submit/`, $(form).serialize(), () => {
//             $("#messageForm").reset();   // reset form fields
//         }
//     );
// }
>>>>>>> 85a52418f61eaf082ddb9193e18aeb808d650d37
