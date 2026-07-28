const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const canvas_div = document.getElementById('canvas_div');

canvas.height = canvas_div.clientHeight;
canvas.width = canvas_div.clientWidth * 0.75;

let x = canvas.width/2, y = canvas.height/2;

const refresh_button = document.getElementById("refresh");
let paused = false;

const pause_button = document.getElementById("pause");

refresh_button.addEventListener("click", () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
});

pause_button.addEventListener("click", () => {

    paused = !paused;

    if (paused) {
        pause_button.textContent = "Unpause";
    }
    else {
        pause_button.textContent = "Pause";
    }

});

function single_frame() {
    let delta_x = (Math.random() - 0.5) * 8;
    let delta_y = (Math.random() - 0.5) * 8;

    if (x + delta_x > canvas.width || x + delta_x < 0) {
        delta_x = -delta_x;
    }

    if (y + delta_y > canvas.height || y + delta_y < 0) {
        delta_y = -delta_y;
    }

    x += delta_x;
    y += delta_y;

    ctx.fillRect(x, y, 2, 2);
}

function draw() {
    if (!paused) {
        single_frame();
    }
    requestAnimationFrame(draw);
}

draw();
