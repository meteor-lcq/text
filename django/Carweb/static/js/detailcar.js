/**
 * Created by Administrator on 2020/3/2.
 */
$(function() {
    //得到当前时间
    var date_now = new Date();
    //得到当前年份
    var year = date_now.getFullYear();
    //得到当前月份
    //注：
    //  1：js中获取Date中的month时，会比当前月份少一个月，所以这里需要先加一
    //  2: 判断当前月份是否小于10，如果小于，那么就在月份的前面加一个 '0' ， 如果大于，就显示当前月份
    var month = date_now.getMonth() + 1 < 10 ? "0" + (date_now.getMonth() + 1) : (date_now.getMonth() + 1);
    //得到当前日子（多少号）
    var date = date_now.getDate() < 10 ? "0" + date_now.getDate() : date_now.getDate();
    //设置input标签的min属性
    $("#order_car_sday").attr("min", year + "-" + month + "-" + date);
});
$(document).ready(function() {
        $('#order_car_sub').click(function(){
            var odate = $("#order_car_fday").val(); //定义变量
            var oday = $("#order_car_sday").val();
            var oaddr=$("#order_car_addr").val();
            var ocarid=$("#order_car_id").val();
            $.ajax({
                url: 'ordercar',
                type: 'POST',
                dataType: 'JSON',
                data: {
                        odate:odate , //服务端请求的数据，前者username代表django获取前端的变量名，后者username代表上面定义的变量名
                        oday: oday,
                        oaddr: oaddr,
                        ocarid: ocarid,
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                },
                success: function (arg){
                    alert(arg.sendpeople);
                }
            })
        })
    })