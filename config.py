#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Anisha Chatterjee

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "8316dbc7-9100-408b-b9a3-b9344f00b613")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "8af7eeb6-0f96-4804-b694-1f798b8c655d")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://qnaserviceapi.azurewebsites.net/qnamaker")
