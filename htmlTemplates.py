css = '''
<style>
.chat-message {
    padding: 10px; 
    border-radius: 15px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    max-width: 80%; 
}


.chat-message.user {
    background-color: #e7f2ea;
    margin-right: auto;
    color: #454545;
}


.chat-message.bot {
    background-color: #1972f5;
    margin-left: auto;
}


.chat-message .avatar {
    margin-right: 0 1px; /* Spacing between avatar and message */
    postion-top: 0;
}

.chat-message .avatar img {
    width: 40px; /* Avatar image width */
    height: 40px; /* Avatar image height */
    border-radius: 50%; /* Circular avatar shape */
    object-fit: cover; /* Maintain aspect ratio */
}

.chat-message .message {
    font-size: 18px; /* Message text size */
    padding: 12px; /* Padding inside the message box */
    border-radius: 10px; /* Rounded corners for message box */
}
body {
    background-image: url('ss.png');
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 48px; max-width: 48px; border-radius: 50%;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
