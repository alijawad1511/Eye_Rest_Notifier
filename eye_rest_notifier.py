from plyer import notification

if __name__=="__main__":
    notification.notify(
        title= "Please Take Eye Rest",
        message= "Eye is a great blessing of God. Save it. Don't waste it. Go and Look far for at least 20 seconds to relax your eyes.",
        app_icon="D:\\Python\\Apps\\RelaxEyesNotification\\eye.ico",
        timeout= 10
    )