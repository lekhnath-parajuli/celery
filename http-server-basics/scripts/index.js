

function fillUserDetails(users) {
    return users.map((user) => {
        return `
        <tr>
            <td> ${user.name} </td>
            <td> ${(new Date(user.createdAt)).toDateString()} </td>
        </tr>
        `;
    });
}

function loadUsers(renderInfo) {
    $(renderInfo.users).load(
        "https://6552de2f5449cfda0f2de0bd.mockapi.io/session/1/users",
        function (response, status, xhr) {
            // to show user required is in progress
            $(renderInfo.loader).detach();
            // fill the dom with users data
            $(renderInfo.users).html(fillUserDetails(JSON.parse(response)));
            // to reduce flicker
            $(renderInfo.userContainer).removeClass("invisible");
        },
    );
}
