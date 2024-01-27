/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let counter = 0
    let current = 0
    for (let i = 0; i < nums.length ; i++){
        if (counter === 0){
            current = nums[i]
            counter += 1
        }else{
            if(current === nums[i]){
                counter += 1
            }else{
                counter -= 1
            }
        }
    }
    return current;
};