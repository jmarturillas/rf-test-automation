"""
IMPORTANT NOTE :
This use case has no automation scripts since the examinee selected the `Use Case #1` to be automated.

The examinee referred to the document of instruction being sent to him.
Here is the line from the document saying about the selection of use case to be automated :

> "Automated test scripts for one of the use cases (of your choice)"



This is to grant the `UseCase2` of the examination.
This file contains the test case applied for the `Cancellation of Subscription`

============= Start of Test Case Creation =============

--------------------------------------------------------------------------------
1.) Name : Validate That The User Has Successfully Kept the Product Subscription
--------------------------------------------------------------------------------

Test Steps :

1. Navigate through the web app login page.
2. Successfully login.
3. Navigate through a product section.
4. Verify that the product section has `Cancel Subscription` link. Otherwise, perform a subscription process to grant
the precondition.
5. Click on the `Cancel Subscription`.
6. Verify that a list of reasons for cancelling the subscription will appear.
7. Click on the desired reason.
8. Click `Continue` button.
9. Verify that the next page contains option for whether `Keep Subscription` or `Cancel Subscription`
10. Click on the `Keep Subscription` button.
11. Verify that the next page contains message that conveys of user remains subscribed together with `50% discount` for {x} amount of months.

--------------------------------------------------------------------------------------
2.) Name : Validate That The User Has Successfully Opt-out of the Product Subscription
--------------------------------------------------------------------------------------

Test Steps :

1. Navigate through the web app login page.
2. Successfully login.
3. Navigate through a product section.
4. Verify that the product section has `Cancel Subscription` link. Otherwise, perform a subscription process to grant
the precondition.
5. Click on the `Cancel Subscription`.
6. Verify that a list of reasons for cancelling the subscription will appear.
7. Click on the desired reason.
8. Click `Continue` button.
9. Verify that the next page contains option for whether `Keep Subscription` or `Cancel Subscription`
10. Click on the `Cancel Subscription` button.
11. Verify that the next page contains message about the subscription being cancelled.

--------------------------------------------------------------------------------------
3.) Name : Validate The Product Subscription is Cancelled
--------------------------------------------------------------------------------------

Test Steps :

1. Navigate through the web app login page.
2. Successfully login.
3. Navigate through a product section.
4. Verify that the product subscription status is `cancelled`

--------------------------------------------------------------------------------------
4. Name : Validate The Product Subscription is Kept Active
--------------------------------------------------------------------------------------

Test Steps :

1. Navigate through the web app login page.
2. Successfully login.
3. Navigate through a product section.
4. Verify that the product subscription status is `active`

--------------------------------------------------------------------------------------
5.) Name : Validate The Discount `Can` be Consumed if the Current Date is Within the Product Subscription Time Span
--------------------------------------------------------------------------------------

Test Steps :

1. Navigate through the web app login page.
2. Successfully login.
3. Navigate through a product section.
4. Verify that the product subscription status is `active`
5. Get the current date value.
6. Get the end-date value in the subscription status.
7. Verify that the current date is not greater than the end-date of subscription.
8. Click on product `Add to Cart` button.
9. Click `Checkout`.
10. Verify that the subscription discount has been consumed successfully.

--------------------------------------------------------------------------------------
6.) Name : Validate The Discount `Cannot` be Consumed if the Current Date is Not Within the Product Subscription Time Span
--------------------------------------------------------------------------------------

Test Steps :

1. Navigate through the web app login page.
2. Successfully login.
3. Navigate through a product section.
4. Verify that the product subscription status is `active`
5. Get the current date value.
6. Get the end-date value in the subscription status.
7. Verify that the current date is not greater than the end-date of subscription.
8. Click on product `Add to Cart` button.
9. Click `Checkout`.
10. Verify that the subscription discount cannot be applied due to one-time usage policy.
11. Verify the message conveying about the subscription usage.


============= End of Test Case Creation =============
"""