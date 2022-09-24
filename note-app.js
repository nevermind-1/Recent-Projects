//targeting element from the DOM
const nums = document.querySelectorAll('.num span')
const counter = document.querySelectorAll('.counter')
const finalMessage = document.querySelector('.final')
const replay = document.querySelector('#replay')

//yet to know the function of this(line 8)
runAnimation()

function resetDOM() {
    counter.classList.remove('hide')
    finalMessage.classList.remove('show')

    nums.forEach((num) => {
        num.classList.value = ''
    })

    nums[0].classList.add('in')
}

function runAnimation(){
    nums.forEach((num,idx) => {
        const nextToLast = nums.length - 1

        num.addEventListener('animationed', (e) => {
            if(e.animationName === 'goIn' && idx !== nextToLast) {
                num.classList.remove('in')
                num.classList.add('out')
            }else if(e.animationName === 'goOut' && num.nextElementSibling) {
                num.nextElementSibling.classList.add('in')
            }else {
                counter.classList.add('hide')
                finalMessage.classList.add('show')
            }
        })
    })
};

replay.addEventListener('click', () => {
    resetDOM()
    runAnimation()
});
