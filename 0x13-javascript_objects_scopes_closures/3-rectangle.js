#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
        if (w > 0 && h > 0) {
            this.height = h;
            this.width = w;
        }
        else {
            return (undefined);
        }
    }
    print () {
        let i = 0;
        while (i < this.heigth) {
            console.log('X'.repeat(this.heigth));
            i++;
        }
    }
};
module.exports = Rectangle;
