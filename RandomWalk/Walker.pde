class Walker {
    float x, y;

    Walker() {
        x = width/2;
        y = height/2;
    }

    void render() {
        stroke(0);
        fill(175);
        ellipseMode(CENTER);
        circle(x, y, 10);
    }

    void walk() {
        float vx = random(-6, 6);
        float vy = random(-6, 6);
        x += vx;
        y += vy;
    }
}