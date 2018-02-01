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
        $('#gazua_order_btn').off("click").on("click", orderClick)

    }

    function checkCanBuy() {
        return $("#side_widget_bankbook .side_widget_content a[title='BTC 거래']").parent().parent().find("td:nth-child(2) span").text() === "0"
    }

    function changeStatus() {
        $('#gazua_order_btn').text(checkCanBuy() ? "매수" : "매도")
    }


    function orderClick() {
        if (checkCanBuy()) {
            buy().then(() => {
                changeStatus()
            })
        } else {
            sell().then(() => {
                changeStatus()
            })
        }
    }

    function buy() {
        return new Promise((resolve) => {
            $("#order_buy_tab").click()
            $("#ask_9 td:nth-child(4)").click()
            $("#limit_buy_max").click()
            $("#limit_order_buy_btn").click()
            let intervalId = setTimeout(func, 500)
            function func() {
                if (!checkCanBuy()) {
                    clearInterval(intervalId)
                    resolve()
                }
            }
        })

    }

    function sell() {
        return new Promise((resolve) => {
            $("#order_sell_tab").click()
            $("#bid_9 td:nth-child(4)").click()
            $("#limit_sell_max").click()
            $("#limit_order_sell_btn").click()
            let intervalId = setTimeout(func, 500)
            function func() {
                if (checkCanBuy()) {
                    clearInterval(intervalId)
                    resolve()
                }
            }
        })

    }
})()
