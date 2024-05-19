
function isReachableAtTime(sx: number, sy: number, fx: number, fy: number, t: number): boolean {

    function traverse(sx: number, sy: number, fx: number, fy: number, t: number): boolean {

        if (t < 0) {
            return false
        }

        if (sx === fx && sy === fy && t === 0) {
            return true
        }

      if (sx < fx) {}

        return traverse(sx + 1, sy, fx, fy, t - 1) ||
        traverse(sx + 1, sy + 1, fx, fy, t - 1) ||
        traverse(sx + 1, sy - 1, fx, fy, t - 1) ||
        traverse(sx - 1, sy + 1, fx, fy, t - 1) ||
        traverse(sx - 1, sy - 1, fx, fy, t - 1) ||
        traverse(sx - 1, sy, fx, fy, t - 1) ||
        traverse(sx, sy + 1, fx, fy, t - 1) ||
        traverse(sx, sy - 1, fx, fy, t - 1)
    }

    return traverse(sx, sy, fx, fy, t)

};

console.log(isReachableAtTime(2, 4, 7, 7, 6) === true)
console.log(isReachableAtTime(1, 2, 1, 2, 1) === false)
