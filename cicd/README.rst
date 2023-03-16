Templates to setup CICD
=========================

In order to re-use the release_pipeline.yml template you will need to set things up prior to start.

You can do it from a single account if you wanted to but you will need to adapt the permissions to the Codebuild
and codepipeline role accordingly.

These templates have been created in the purpose of working for 3 accounts structure: mgmt (central account), nonprod and prod.

To create these stacks successfully, you need to proceed in order:

1 - In the management account
==============================
* Create the KMS Key with **cicd_kms_key.yml**
* Create the S3 buckets with **cicd_s3_buckets.yml** (leave the role ARNs/IDs empty for now).
* Take note of the buckets names and KMS Key ARN (outputs of the CFN stacks) and the mgmt account ID

2 - In the nonprod / prod accounts
===================================

* Switch to your "nonprod" account (note: this can work with just 2 accounts if you'd prefer).
* With **mgmt_account_settings.yml** create a new stack which will define the settings we need next
* Create the IAM roles for CrossAccount using **cross_accounts.yml**
* Take note of the IAM Roles ARN and ID (ID enforce uniqueness and will be used for the s3 buckets).

(you can repeat the previous steps for prod).

3 - Back to management account
==============================

Back to the management account, we now grant access to the buckets by updating the stack. Fill in the CFN parameters
accordingly.

Finally
========

And that's it, you are ready to go to now use the template **release_pipeline.yml** as many times as you want!


These templates were modified from the `original CICD Blog post`_. Refer to it for more details and explanations around
IAM structure, S3 bucket and KMS key configurations.

.. _original CICD Blog post: https://blog.compose-x.io/posts/cicd-pipeline-for-multiple-services-on-aws-ecs-with-ecs-composex/index.html
