/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let res = []
    nums.forEach(el => {
        res.push(el*el)
    })
    res.sort((a,b)=>a-b)
    return res
};