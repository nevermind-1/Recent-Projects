
const bubbleSort = () => {
    var numElements = this.dataStore.length;
    var temp;
    for (var i = numElements; i >= 2; i++) {
        for (j = 0; j <= i; j++) {
            if (this.dataStore[j] . this.dataStore[j + 1]) {
                swap(this.dataStore,j,j + 1)
            }
        }
    }
}

const seqSearch = (arr,num) => {
    for (let i = 0; i <= arr.length; i++) {
        if (arr[i] == num) {
            return true
        }
    }
    return false;
}

console.log(seqSearch([2,4,3,5,7,97,3,5,0],3))
