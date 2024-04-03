/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var reverseStr = function (s, k) {
    if (k > s.length) return s.split("").reverse().join("")
    res = ""
    let toReverse=true
    for(i=0; i<s.length; i++){
        if((i+1)%k==0){
            const sub=s.slice(i+1-k,i+1)
            if(toReverse){
                res+=sub.split('').reverse().join("")
            } else{
                res+=sub
            }
            toReverse = !toReverse
        }
    }
    if(res.length<s.length){
        const sub = s.slice(res.length)
        if(toReverse){
            res+=sub.split('').reverse().join("")
        }else{
            res+=sub
        }
    }
    return res

};