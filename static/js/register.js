let q = document.querySelector('input[name="phone"]');
q.addEventListener('keydown', () => {
    console.log(q.value);
    if (!(q.value in ['', '+']) && q.value[-1] in ['+', '-', '(', '=', ')', '/', '{', '}', '[', ']']) q.value[-1] = '';
    q.value = q.value.slice(0, q.value[0] == '+' ? 11 : 10);
})