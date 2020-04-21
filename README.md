# sns-to-slack

Post SNS messages to Slack.

## Install

```sh
$ npm install
```

## Deploy

Before deploy, required to export environment variables.

```sh
export ENCRYPTED_SLACK_WEBHOOK="xxxxx"
export TOPIC="arn:aws:sns:ap-northeast-1:xxxxxxxxxxxx:yyyyyyy"
```

`ENCRYPTED_SLACK_WEBHOOK` must be encrypted by KMS like this.

```sh
$ aws kms encrypt --key-id alias/default --plaintext fileb://slack-webhook.txt --query CiphertextBlob --output text
```

Deploy to development.

```sh
$ npx sls deploy -v
```

Deploy to production.

```sh
$ npx sls deploy -v --stage prod
```

## Cleanup

Development.

```sh
$ npx sls remove
```

Production.

```sh
$ npx sls remove --stage prod
```
