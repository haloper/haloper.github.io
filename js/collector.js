(function () {
  alert('Import collector')
  setInterval(() => {
    let obj = getInfo()
    let now = Math.floor((new Date()).getTime() / (1000 * 60))
    let log = now
              + "," + obj.ask5.price
              + "," + obj.ask5.count
              + "," + obj.ask4.price
              + "," + obj.ask4.count
              + "," + obj.ask3.price
              + "," + obj.ask3.count
              + "," + obj.ask2.price
              + "," + obj.ask2.count
              + "," + obj.ask1.price
              + "," + obj.ask1.count
              + "," + obj.bid1.price
              + "," + obj.bid1.count
              + "," + obj.bid2.price
              + "," + obj.bid2.count
              + "," + obj.bid3.price
              + "," + obj.bid3.count
              + "," + obj.bid4.price
              + "," + obj.bid4.count
              + "," + obj.bid5.price
              + "," + obj.bid5.count
    sendLog(log).then((data) => {
      console.log(data)
    })
  }, 1000 * 60)

  function sendLog (log) {
    return $.ajax({ url: 'http://localhost:9080?data=' + log
        , dataType: 'jsonp'
        , jsonpCallback: "jcallback"
    });

  }

  function getInfo () {
    let table = $("#market_stat_table_wrapper")
    return {
      ask5: getAsk(table.find("tr#ask_5")),
      ask4: getAsk(table.find("tr#ask_4")),
      ask3: getAsk(table.find("tr#ask_3")),
      ask2: getAsk(table.find("tr#ask_2")),
      ask1: getAsk(table.find("tr#ask_1")),
      bid1: getBid(table.find("tr#bid_1")),
      bid2: getBid(table.find("tr#bid_2")),
      bid3: getBid(table.find("tr#bid_3")),
      bid4: getBid(table.find("tr#bid_4")),
      bid5: getBid(table.find("tr#bid_5"))
    }
  }

  function getAsk (tr) {
    let price = tr.find(":nth-child(4)").text()
    let count = tr.find(":nth-child(2)").text() + tr.find(":nth-child(3)").text()
    return {
      price: price.replace(/\,/g, ''),
      count: count
    }
  }

  function getBid (tr) {
    let price = tr.find(":nth-child(4)").text()
    let count = tr.find(":nth-child(5)").text() + tr.find(":nth-child(6)").text()
    return {
      price: price.replace(/\,/g, ''),
      count: count
    }
  }
})()
