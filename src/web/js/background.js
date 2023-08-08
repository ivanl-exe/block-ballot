$().ready(() => {
    console.log(`v${$().jquery}`);

    const canvas = $("#background");
    const canvasDOM = canvas.get(0);
    const ctx = canvasDOM.getContext("2d");

    const resize = () => {
        ctx.canvas.width = canvas.width();
        ctx.canvas.height = canvas.height();    
    }
    resize();
    
    $(window).on("resize", () => resize());

    $(document).on("mousemove", (e) => {
        const [x, y] = [e.pageX, e.pageY];
        const maxRadius = 100;
        nap(100).then(() => {
            clear();
            orb([x, y], maxRadius);
        });
    });

    const clear = () => {
        ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    }

    const orb = ([x, y], maxRadius) => {
        for(let radius = 0; radius <= maxRadius; radius++) {
            ctx.beginPath();
            ctx.arc(x, y, radius, 2 * Math.PI, false);
            ctx.lineWidth = 5;
            const n = Math.pow(maxRadius - radius, 2) / Math.pow(maxRadius, 2) * (255 - 0);
            ctx.strokeStyle = `rgba(${Array(4).fill(n).join(", ")})`;
            ctx.stroke();
        }
    }
});