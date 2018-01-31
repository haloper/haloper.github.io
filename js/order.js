(() => {
    alert('Import order')
    const html = `
        <div style="width: 300px; height: 120px; position: fixed; top:300px; left:calc(50% - 150px); background-color: rgba(0,0,0,.4); z-index:999">
            <div style="float:right"><button id="gazua_close">X</button></div>
            <div style="position: absolute;top: 32px;left: 23px;">
                <button id="gazua_order_btn" style="width: 250px;height: 60px;">주문</button>
            </div>
        </div>
    `
    $('body').append(html)
    attachEvent()

    function attachEvent() {

    }
})()
