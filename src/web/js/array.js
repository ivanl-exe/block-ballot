Array.prototype.copy = function() { this.slice(); } 

Array.prototype.zfill = function(n, filler = 0) {
    if(n > this.length) {
        return this.concat(Array(n - this.length).fill(filler));
    }
    return this;
};