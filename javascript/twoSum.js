/**
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 * @param {number[]} arr
 * @param {number} target
 * @return {number[]}
 */
function twoSum(arr, target) {
    const map = {}
    const resp = Array.from({length: 2})
    for(let idx in arr) {
        const complement = target - arr[idx]
        if (map.get(complement)) {
            resp[0] = map.get(complement)
            resp[1] = idx
            return resp
        } else {
            map.set(arr[idx], idx)
        }
    }
}

console.log(twoSum([2,1,3,5,8], 10))