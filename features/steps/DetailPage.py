from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import json

with open('D:\BehaveProject\cred.json') as f:
    data = json.load(f)

@when('the user opens the brand detail page')
def openPage(context):
    time.sleep(3)
    context.driver.get(data['pkbrand'])


@then('Verify Brand Card')
# Card Image + Card Content
def card(context):
    time.sleep(3)
    card = context.driver.find_element(By.CSS_SELECTOR, '.b_card')
    if card.is_displayed():
        print("Brand Card Found")

    time.sleep(2)
    img = context.driver.find_element(By.CSS_SELECTOR, '.b_card img')
    if img.is_displayed():
        print(" ")
        print("Brand Image Found")

    time.sleep(2)
    cont = context.driver.find_element(By.CSS_SELECTOR, '.b_card')
    if cont.is_displayed():
        print(" ")
        print(cont.text)


@then('Verify Banner & breadcrump')
# banner + breadcrumb
def banner(context):
    time.sleep(2)
    banner = context.driver.find_element(By.CSS_SELECTOR, '.brand-banner')
    if banner.is_displayed():
        print(" ")
        print("Banner is available")


    time.sleep(2)
    breadcrumb = context.driver.find_elements(By.CSS_SELECTOR, ".breadcrumb li a")
    for name in breadcrumb:
        print(" ")
        print(name.text)
        print(name.get_attribute('href'))


@then('Order Progress Bar + Max Cashback')
# Order Progress Bar + Max Cashback
def cashback(context):
    time.sleep(2)

    CB = context.driver.find_elements(By.CSS_SELECTOR, '.step-parent span')
    print(" ")
    for steps in CB:
        print(steps.text)

    time.sleep(2)
    AMD = context.driver.find_elements(By.CSS_SELECTOR, '.cashback-card-content-box p')
    print(" ")
    for steps in AMD:
        print(steps.text)


@then('About Section is Visible')
# About + Specialities + You May Also Like
def About(context):
    time.sleep(2)

    about = context.driver.find_element(By.CSS_SELECTOR, '.right-section .readmorecontent p')
    print(" ")
    print(about.text)


@then('Specialities Section is Visible')
def Specialities(context):

    special = context.driver.find_element(By.CSS_SELECTOR, 'div.mt-4.mb-4.detail_box')
    print(" ")
    print(special.text)
    print(" ")


@then('You May Also Like Section is Visible')
def YMAL(context):

    print("You May Also Like Brands Are")
    sections = context.driver.find_elements(By.CSS_SELECTOR, '#brand-detail .c_card h3')
    for section in sections:
        print(" ")
        if section.is_displayed():
            print(section.text)


@then('Other User Ratings are Visible')
# Other User Ratings
def Rating(context):
    time.sleep(2)
    print(" ")
    print("Outlet Rating are")
    print(" ")

    section = context.driver.find_element(By.CSS_SELECTOR, '.outlet_rating')
    context.driver.execute_script("return arguments[0].scrollIntoView(true);", section)
    rating = section.text
    rate = rating.split()
    print("Average Rating is " + rate[2])
    print("User who Submitted the " + rate[5])
    print("User who Submitted the " + rate[6])


@then('Other Users Reviews are Visible')
# Other Users Reviews
def Reviews(context):
    time.sleep(2)
    rating = 0

    users = context.driver.find_elements(By.CSS_SELECTOR, '.review .c_row .media h5')
    for user in users:
        elem = context.driver.find_elements(By.CSS_SELECTOR, '.review .c_row star-rating div')[rating]
        print(user.text)
        time.sleep(2)
        print("Submit the rating with " + elem.get_attribute('title') + " Star")
        rating += 1


@then('Delete Own Review')
# Delete Own Review
def deleteReview(context):
    time.sleep(3)
    try:
        review = context.driver.find_element(By.CSS_SELECTOR, '.delete_review_btn')
        if review.is_displayed():
            time.sleep(2)
            delete_review = context.driver.find_element(By.CSS_SELECTOR, '.delete_review_btn')
            delete_review.click()
            time.sleep(3)
            print("Review Has Been Deleted")
            context.driver.find_element(By.CSS_SELECTOR, '#deleteRecentReviewModal button.btn.btn-danger').click()
    except NoSuchElementException:
        print("Your Review Not Exist")


@then('Write a Review')
# Write a Review
def writeReview(context):
    time.sleep(5)
    addrev = context.driver.find_element(By.CSS_SELECTOR, '#user-review-rating > div.rate-base-layer > span:nth-child(4)')
    context.driver.execute_script("return arguments[0].scrollIntoView(true);", addrev)
    if addrev.is_displayed():
        addrev.click()
        time.sleep(2)
        desc = context.driver.find_element(By.CSS_SELECTOR, '#comment')
        desc.click()
        time.sleep(2)
        desc.send_keys("daraz is wonderful app and all user use this but this time savyour give Cashback so we are very thankful to savyour app for amazing discounts and offers and hope more offers in coming soon. jazakallah")
        time.sleep(2)
        image = context.driver.find_element(By.CSS_SELECTOR, '.dz-button')
        print("Selecting Image For Adding Review")
        time.sleep(2)

        image.send_keys(os.getcwd() + '\image.jpg')
        time.sleep(2)

        image.send_keys(os.getcwd() + '\image2.jpg')
        time.sleep(2)

        image.send_keys(os.getcwd() + '\image3.jpg')
        time.sleep(2)
        time.sleep(3)

        context.driver.find_element(By.CSS_SELECTOR, '#add-review-submit').click()
        time.sleep(10)
        print("Review Added Successfully")

        context.driver.find_element(By.CSS_SELECTOR, '#congratulateModal .step-1 button').click()

@then('Adding Comment on Review')
# Adding Comment on Review
def adding_comment_on_review(context):
    time.sleep(5)
    comsec = context.driver.find_element(By.CSS_SELECTOR, '.user-comment-button')
    context.driver.execute_script("return arguments[0].scrollIntoView(true);", comsec)
    if comsec.is_displayed():
        comsec.click()
        element = context.driver.find_element(By.CSS_SELECTOR, '.user-comment-button')
        data_id_value = element.get_attribute('data-id')
        comment = context.driver.find_element(By.CSS_SELECTOR, '#new-user-comment-'+str(data_id_value)+' > form > div > textarea')
        comment.click()
        time.sleep(2)
        comment.send_keys("Good Review")
        time.sleep(2)
        comment.send_keys(Keys.RETURN)
        time.sleep(2)
        print("Comment Has Been Added")


@then('Like Comment')
# Like Comment & Review
def like_comment(context):
    time.sleep(3)
    try:
        liksec = context.driver.find_element(By.CSS_SELECTOR, '.comment-helpful-button')
        context.driver.execute_script("return arguments[0].scrollIntoView(true);", liksec)
        if liksec.is_displayed():
            time.sleep(2)
            liksec.click()
            print("Comment Marked Helpful")
    except NoSuchElementException:
        print("Like Button Not Exist")


@then('Delete Comment if Exist')
# Delete Comment if Exist
def deleting_review_comment_if_exist(context):
    time.sleep(3)
    try:
        fc = context.driver.find_element(By.CSS_SELECTOR, '.comment-delete-button')
        context.driver.execute_script("return arguments[0].scrollIntoView(true);", fc)
        if fc.is_displayed():
            fc.click()
            time.sleep(2)
            context.driver.find_element(By.CSS_SELECTOR, '#deleteComment').click()
            print("Your Previous Comment Has Been Deleted")
    except NoSuchElementException:
        print("Delete Comment Button Not Exist")

