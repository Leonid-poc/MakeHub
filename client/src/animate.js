const animItems = () => {
    const items = document.getElementsByClassName('_animate_obj');
    console.log(items)
    if (items.length > 0) {
        window.addEventListener('scroll', animOnScroll);

        const animOnScroll = () => {
            for (let i = 0; i < items.length; i++) {
                const animItem = items[i];
                const animItemHeight = animItem.offsetHeight;
                const animItemOffset = offset(animItem).top;
                const animStart = 4;

                console.log(i)

                let animItemPoint = window.innerHeight - animItemHeight / animStart;

                if (animItemHeight > window.innerHeight) {
                    animItemPoint = window.innerHeight - window.innerHeight / animStart; 
                }

                if ((window.pageYOffset > animItemOffset - animItemPoint) && window.pageYOffset < (animItemOffset + animItemHeight)) {
                    animItem.classList.add('_animation_active');
                } else {
                    animItem.classList.remove('_animation_active');
                }
            }
        }

        const offset = (el) => {
            const rect = el.getBoundingClientRect(),
                scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
                scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            return { top: rect.top + scrollTop, left: rect.left + scrollLeft }    
        }

        setTimeout(() => {
            animOnScroll();
        }, 300);
    }
}

export default animItems