$().ready(() => {
    setInterval(() => {
        const timestamp = Math.floor(Date.now() / 1000);
        $("#clock").text(timestamp.toString());
    }, 1000)
});