$(document).ready(function(){

    login_form = $('#login_form')
    reg_form = $('#reg_form')

    $('.register_head').click(function(){

        $('.head_under_line').css({
            'transform':'translatex(108px)',
            'width':'5.5rem'
        })

        login_form.css('transform','translatex(500px)')
        reg_form.css('transform','translatex(500px)')
    })

    $('.login_head').click(function(){

        $('.head_under_line').css({
            'transform':'translatex(0)',
            'width':'4rem'
        })

        login_form.css('transform','translatex(0)')
        reg_form.css('transform','translatex(0)')
    })

    // adding correct messages to the message container

    $.fn.MessageManager = function(msg){

        msg_container = $('.message_container')
        msg_container.css('opacity',1)

        if(msg.success){
            msg_container.text(msg.success)
            msg_container.removeClass('error')
            msg_container.addClass('success')

        }
        else{
            msg_container.text(msg.error)
            msg_container.removeClass('success')
            msg_container.addClass('error')
        }

        setTimeout(function(){
            msg_container.css('opacity',0)
        },2000)
    }

    // login or register form submission

    $('.form').submit(function(e){
        e.preventDefault()
        form = $(this)
        url = form.attr('action')
        data = form.serialize()
        form[0].reset()
        $.ajax({
            url:url,
            data:data,
            method:'POST',
            success:function(response){

                if(response.success||response.error){
                    $.fn.MessageManager(response)
                }
                else{
                    window.location.href=response.url
                }
               
            },
            error:function(error,xhr){

                console.log('Ajax error : ',error,'\n','xhr : ',xhr)
            }
        })
    })


    // create and download pdf of booking details

    
})

