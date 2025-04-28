juspay_session_schema = {
    "type": "object",
    "required": [
        "order_id", "amount", "customer_id", "customer_email",
        "customer_phone", "payment_page_client_id", "action", "return_url"
    ],
    "properties": {
        "order_id": {"type": "string", "description": "Unique Identifier for the order (Max 21 Alphanumeric)."},
        "amount": {"type": "string", "description": "Amount customer has to pay (e.g., '1.00')."},
        "customer_id": {"type": "string", "description": "Unique merchant identifier for the customer."},
        "customer_email": {"type": "string", "description": "Customer's email address."},
        "customer_phone": {"type": "string", "description": "Customer's mobile number."},
        "payment_page_client_id": {"type": "string", "description": "Unique merchant identifier provided by Juspay."},
        "action": {"type": "string", "enum": ["paymentPage", "paymentManagement"], "description": "Action to be performed, e.g., 'paymentPage'."},
        "return_url": {"type": "string", "description": "URL for redirection post payment."},
        "description": {"type": "string", "description": "Order description for user.", "isRequired": "False"},
        "first_name": {"type": "string", "description": "Customer's first name.", "isRequired": "False"},
        "last_name": {"type": "string", "description": "Customer's last name.", "isRequired": "False"},
        "mobile_country_code": {"type": "string", "description": "Mobile country code without '+'", "isRequired": "False"},
        "udf1": {"type": "string", "description": "User defined field 1.", "isRequired": "False"},
    },
}

juspay_order_status_schema = {
   "type": "object",
   "required": ["order_id"],
   "properties": {
       "order_id": {
           "type": "string",
           "description": "Unique identifier for the order to check its status."
       },
   }
}

juspay_refund_schema = {
    "type": "object",
    "required": ["order_id", "unique_request_id", "amount"],
    "properties": {
        "order_id": {
            "type": "string",
            "description": "Unique identifier of the order to refund."
        },
        "unique_request_id": {
            "type": "string",
            "description": "Unique refund request identifier (e.g., 'xyz123')."
        },
        "amount": {
            "type": "string",
            "description": "Refund amount as a string (e.g., '100.00')."
        }
    },
}


juspay_get_customer_schema = {
    "type": "object",
    "required": ["customer_id"],
    "properties": {
        "customer_id": {
            "type": "string",
            "description": "Unique identifier of the customer."
        }
    }
}

juspay_create_customer_schema = {
    "type": "object",
    "required": ["object_reference_id", "mobile_number", "email_address"],
    "properties": {
        "object_reference_id": {
            "type": "string",
            "description": "Unique reference ID for the customer (typically email address)."
        },
        "mobile_number": {
            "type": "string",
            "description": "Customer's mobile number without country code."
        },
        "email_address": {
            "type": "string",
            "description": "Customer's email address."
        },
        "first_name": {
            "type": "string",
            "description": "Customer's first name."
        },
        "last_name": {
            "type": "string",
            "description": "Customer's last name."
        },
        "mobile_country_code": {
            "type": "string",
            "description": "Mobile country code without '+' (e.g., '91')."
        },
        "get_client_auth_token": {
            "type": "boolean",
            "description": "Set to true to get client authentication token in response.",
            "default": False
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_update_customer_schema = {
    "type": "object",
    "required": ["customer_id"],
    "properties": {
        "customer_id": {
            "type": "string",
            "description": "Juspay customer ID to update (starts with 'cst_')."
        },
        "mobile_number": {
            "type": "string",
            "description": "Updated mobile number."
        },
        "email_address": {
            "type": "string",
            "description": "Updated email address."
        },
        "first_name": {
            "type": "string",
            "description": "Updated first name."
        },
        "last_name": {
            "type": "string",
            "description": "Updated last name."
        },
        "mobile_country_code": {
            "type": "string",
            "description": "Updated mobile country code without '+' (e.g., '91')."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_create_order_schema = {
    "type": "object",
    "required": [
        "order_id", "amount", "currency", "customer_id", 
        "customer_email", "customer_phone", "return_url"
    ],
    "properties": {
        "order_id": {
            "type": "string",
            "description": "Unique identifier for the order (max 21 alphanumeric chars)."
        },
        "amount": {
            "type": "string", 
            "description": "The order amount (e.g., '100.00')."
        },
        "currency": {
            "type": "string",
            "description": "Currency code (e.g., 'INR')."
        },
        "customer_id": {
            "type": "string",
            "description": "Merchant's identifier for the customer."
        },
        "customer_email": {
            "type": "string",
            "description": "Customer's email address."
        },
        "customer_phone": {
            "type": "string",
            "description": "Customer's phone number."
        },
        "return_url": {
            "type": "string",
            "description": "URL to redirect after payment."
        },
        "description": {
            "type": "string",
            "description": "Description of the order."
        },
        "product_id": {
            "type": "string",
            "description": "Product identifier."
        },
        "get_client_auth_token": {
            "type": "boolean",
            "description": "Whether to get client auth token in response.",
            "default": False 
        },
        "billing_address_first_name": {"type": "string", "description": "Billing first name"},
        "billing_address_last_name": {"type": "string", "description": "Billing last name"},
        "billing_address_line1": {"type": "string", "description": "Billing address line 1"},
        "billing_address_line2": {"type": "string", "description": "Billing address line 2"},
        "billing_address_line3": {"type": "string", "description": "Billing address line 3"},
        "billing_address_city": {"type": "string", "description": "Billing city"},
        "billing_address_state": {"type": "string", "description": "Billing state"},
        "billing_address_country": {"type": "string", "description": "Billing country"},
        "billing_address_postal_code": {"type": "string", "description": "Billing postal code"},
        "billing_address_phone": {"type": "string", "description": "Billing phone"},
        "billing_address_country_code_iso": {"type": "string", "description": "Billing country ISO code"},
        
        "shipping_address_first_name": {"type": "string", "description": "Shipping first name"},
        "shipping_address_last_name": {"type": "string", "description": "Shipping last name"},
        "shipping_address_line1": {"type": "string", "description": "Shipping address line 1"},
        "shipping_address_line2": {"type": "string", "description": "Shipping address line 2"},
        "shipping_address_line3": {"type": "string", "description": "Shipping address line 3"},
        "shipping_address_city": {"type": "string", "description": "Shipping city"},
        "shipping_address_state": {"type": "string", "description": "Shipping state"},
        "shipping_address_country": {"type": "string", "description": "Shipping country"},
        "shipping_address_postal_code": {"type": "string", "description": "Shipping postal code"},
        "shipping_address_phone": {"type": "string", "description": "Shipping phone"},
        "shipping_address_country_code_iso": {"type": "string", "description": "Shipping country ISO code"},
        
        "routing_id": {
            "type": "string", 
            "description": "Optional custom routing ID for the API request."
        },
    },
    "additionalProperties": True
}

juspay_update_order_schema = {
    "type": "object",
    "required": ["order_id"],
    "properties": {
        "order_id": {
            "type": "string",
            "description": "Juspay order ID to update."
        },
        "amount": {
            "type": "string",
            "description": "Updated order amount (e.g., '90.00')."
        },
        "currency": {
            "type": "string",
            "description": "Updated currency code."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    },
    "additionalProperties": True
}

juspay_order_fulfillment_schema = {
    "type": "object",
    "required": ["order_id", "fulfillment_status", "fulfillment_command", "fulfillment_time", "fulfillment_id"],
    "properties": {
        "order_id": {
            "type": "string",
            "description": "Unique identifier of the order to update fulfillment status."
        },
        "fulfillment_status": {
            "type": "string",
            "enum": ["SUCCESS", "FAILURE", "PENDING"],
            "description": "Status of the fulfillment (SUCCESS, FAILURE, PENDING)."
        },
        "fulfillment_command": {
            "type": "string",
            "enum": ["NO_ACTION", "RELEASE_HOLD", "HOLD"],
            "description": "Command for the fulfillment action."
        },
        "fulfillment_time": {
            "type": "string",
            "format": "date-time",
            "description": "Time of fulfillment in ISO format (e.g., '2024-07-08T16:30:33')."
        },
        "fulfillment_id": {
            "type": "string",
            "description": "Unique identifier for this fulfillment action."
        },
        "fulfillment_data": {
            "type": "string",
            "description": "Optional metadata for the fulfillment."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_txn_refund_schema = {
    "type": "object",
    "required": ["txn_id", "unique_request_id", "amount"],
    "properties": {
        "txn_id": {
            "type": "string",
            "description": "Transaction ID to be refunded (e.g., 'merchant_id-order_id-1')."
        },
        "unique_request_id": {
            "type": "string",
            "description": "Unique identifier for this refund request."
        },
        "amount": {
            "type": "string",
            "description": "Refund amount as a string (e.g., '100.00')."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_create_txn_schema = {
    "type": "object",
    "required": ["order.order_id", "order.amount", "order.currency", "order.customer_id", 
                "payment_method_type", "order.return_url", "merchant_id"],
    "properties": {
        "order.order_id": {
            "type": "string",
            "description": "Unique identifier for the order (max 21 alphanumeric chars)."
        },
        "order.amount": {
            "type": "string", 
            "description": "The order amount (e.g., '100.00')."
        },
        "order.currency": {
            "type": "string",
            "description": "Currency code (e.g., 'INR')."
        },
        "order.customer_id": {
            "type": "string",
            "description": "Merchant's identifier for the customer."
        },
        "order.customer_email": {
            "type": "string",
            "description": "Customer's email address."
        },
        "order.customer_phone": {
            "type": "string",
            "description": "Customer's phone number."
        },
        "order.return_url": {
            "type": "string",
            "description": "URL to redirect after payment."
        },
        "merchant_id": {
            "type": "string",
            "description": "Your merchant ID provided by Juspay."
        },
        "payment_method_type": {
            "type": "string",
            "enum": ["CARD", "NB", "WALLET", "UPI", "EMI"],
            "description": "Type of payment method."
        },
        "payment_method": {
            "type": "string",
            "description": "Specific payment method (e.g., 'VISA', 'MASTERCARD')."
        },
        "card_number": {
            "type": "string",
            "description": "Card number (for CARD payment method)."
        },
        "card_exp_month": {
            "type": "string",
            "description": "Card expiry month (e.g., '05')."
        },
        "card_exp_year": {
            "type": "string",
            "description": "Card expiry year (e.g., '25')."
        },
        "name_on_card": {
            "type": "string",
            "description": "Name as printed on the card."
        },
        "card_security_code": {
            "type": "string",
            "description": "Card CVV/security code."
        },
        "save_to_locker": {
            "type": "boolean",
            "description": "Whether to save card details for future use."
        },
        "redirect_after_payment": {
            "type": "boolean",
            "description": "Whether to redirect to return URL after payment."
        },
        "format": {
            "type": "string",
            "enum": ["json"],
            "description": "Response format, typically 'json'."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    },
    "additionalProperties": True
}

juspay_create_moto_txn_schema = {
    "type": "object",
    "required": ["order.order_id", "order.amount", "order.currency", "order.customer_id", 
                "payment_method_type", "order.return_url", "merchant_id", "auth_type"],
    "properties": {
        "order.order_id": {
            "type": "string",
            "description": "Unique identifier for the order."
        },
        "order.amount": {
            "type": "string", 
            "description": "The order amount (e.g., '100.00')."
        },
        "order.currency": {
            "type": "string",
            "description": "Currency code (e.g., 'INR')."
        },
        "order.customer_id": {
            "type": "string",
            "description": "Merchant's identifier for the customer."
        },
        "order.return_url": {
            "type": "string",
            "description": "URL to redirect after payment."
        },
        "merchant_id": {
            "type": "string",
            "description": "Your merchant ID provided by Juspay."
        },
        "payment_method_type": {
            "type": "string",
            "enum": ["CARD"],
            "description": "Type of payment method (only CARD for MOTO)."
        },
        "payment_method": {
            "type": "string",
            "description": "Specific payment method (e.g., 'VISA', 'MASTERCARD')."
        },
        "card_number": {
            "type": "string",
            "description": "Card number (masked or full)."
        },
        "card_exp_month": {
            "type": "string",
            "description": "Card expiry month (e.g., '05')."
        },
        "card_exp_year": {
            "type": "string",
            "description": "Card expiry year (e.g., '26')."
        },
        "redirect_after_payment": {
            "type": "boolean",
            "description": "Whether to redirect to return URL after payment."
        },
        "format": {
            "type": "string",
            "enum": ["json"],
            "description": "Response format, typically 'json'."
        },
        "auth_type": {
            "type": "string",
            "enum": ["MOTO"],
            "description": "Authentication type, must be 'MOTO'."
        },
        "tavv": {
            "type": "string",
            "description": "Transaction Authentication Verification Value for MOTO transactions."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    },
    "additionalProperties": True
}

juspay_add_card_schema = {
    "type": "object",
    "required": [
        "merchant_id", "customer_id", "customer_email", 
        "card_number", "card_exp_year", "card_exp_month", "name_on_card"
    ],
    "properties": {
        "merchant_id": {
            "type": "string",
            "description": "Merchant identifier."
        },
        "customer_id": {
            "type": "string",
            "description": "Customer identifier."
        },
        "customer_email": {
            "type": "string",
            "description": "Customer's email address."
        },
        "card_number": {
            "type": "string",
            "description": "Complete card number."
        },
        "card_exp_year": {
            "type": "string",
            "description": "Card expiry year (e.g., '2025')."
        },
        "card_exp_month": {
            "type": "string",
            "description": "Card expiry month (e.g., '07')."
        },
        "name_on_card": {
            "type": "string",
            "description": "Name as printed on the card."
        },
        "nickname": {
            "type": "string",
            "description": "Friendly name for the card."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_list_cards_schema = {
    "type": "object",
    "required": ["customer_id"],
    "properties": {
        "customer_id": {
            "type": "string",
            "description": "Customer identifier whose cards to retrieve."
        },
        "options.check_cvv_less_support": {
            "type": "boolean",
            "description": "Check if cards support CVV-less transactions.",
            "default": False
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_delete_card_schema = {
    "type": "object",
    "required": ["card_token"],
    "properties": {
        "card_token": {
            "type": "string",
            "description": "Unique token of the card to be deleted."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_update_card_schema = {
    "type": "object",
    "required": ["card_token"],
    "properties": {
        "card_token": {
            "type": "string",
            "description": "Unique token of the card to be updated."
        },
        "nickname": {
            "type": "string",
            "description": "New friendly name for the card."
        },
        "customer_id": {
            "type": "string",
            "description": "Customer identifier associated with the card."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_card_info_schema = {
    "type": "object",
    "required": ["bin"],
    "properties": {
        "bin": {
            "type": "string",
            "description": "First 6-9 digits of the card number (BIN)."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_bin_list_schema = {
    "type": "object",
    "properties": {
        "auth_type": {
            "type": "string",
            "description": "Authentication type (e.g., 'OTP').",
            "default": "OTP"
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_saved_payment_methods_schema = {
    "type": "object",
    "required": ["customer_id"],
    "properties": {
        "customer_id": {
            "type": "string",
            "description": "Unique identifier of the customer whose payment methods to retrieve."
        },
        "payment_method": {
            "type": "array",
            "description": "List of payment method types to retrieve.",
            "items": {
                "type": "string",
                "enum": ["UPI_COLLECT"]
            },
            "default": ["UPI_COLLECT"]
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_upi_collect_schema = {
    "type": "object",
    "required": ["order_id", "merchant_id", "upi_vpa"],
    "properties": {
        "order_id": {
            "type": "string",
            "description": "Unique identifier for the order."
        },
        "merchant_id": {
            "type": "string",
            "description": "Merchant identifier."
        },
        "upi_vpa": {
            "type": "string",
            "description": "UPI Virtual Payment Address of the customer."
        },
        "redirect_after_payment": {
            "type": "boolean",
            "description": "Whether to redirect after payment.",
            "default": True
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_verify_vpa_schema = {
    "type": "object",
    "required": ["vpa", "merchant_id"],
    "properties": {
        "vpa": {
            "type": "string",
            "description": "UPI Virtual Payment Address to verify."
        },
        "merchant_id": {
            "type": "string",
            "description": "Merchant identifier."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_upi_intent_schema = {
    "type": "object",
    "required": ["order_id", "merchant_id"],
    "properties": {
        "order_id": {
            "type": "string",
            "description": "Unique identifier for the order."
        },
        "merchant_id": {
            "type": "string",
            "description": "Merchant identifier."
        },
        "upi_app": {
            "type": "string",
            "description": "Specific UPI app to open (e.g., 'com.phonepe.app')."
        },
        "sdk_params": {
            "type": "boolean",
            "description": "Whether to include SDK parameters in the response.",
            "default": True
        },
        "redirect_after_payment": {
            "type": "boolean",
            "description": "Whether to redirect after payment.",
            "default": True
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_list_offers_schema = {
    "type": "object",
    "required": ["order", "payment_method_info"],
    "properties": {
        "order": {
            "type": "object",
            "required": ["order_id", "amount", "currency"],
            "properties": {
                "order_id": {"type": "string", "description": "Unique identifier for the order."},
                "amount": {"type": "string", "description": "Order amount as a string (e.g., '12000')."},
                "currency": {"type": "string", "description": "Currency code (e.g., 'INR')."}
            }
        },
        "payment_method_info": {
            "type": "array",
            "description": "List of payment methods to check offer eligibility for.",
            "items": {
                "type": "object",
                "properties": {
                    "payment_method_type": {"type": "string", "description": "Type of payment method (e.g., 'CARD', 'UPI')."},
                    "payment_method_reference": {"type": "string", "description": "Reference identifier for the payment method."},
                    "payment_method": {"type": "string", "description": "Specific payment method (e.g., 'VISA', 'UPI')."},
                    "card_number": {"type": "string", "description": "Card number (for CARD payment method)."},
                    "bank_code": {"type": "string", "description": "Bank code (for CARD payment method)."},
                    "card_type": {"type": "string", "description": "Type of card (e.g., 'CREDIT', 'DEBIT')."},
                    "card_token": {"type": "string", "description": "Card token for saved cards."},
                    "upi_vpa": {"type": "string", "description": "UPI Virtual Payment Address (for UPI payment method)."},
                    "upi_app": {"type": "string", "description": "UPI app package name (for UPI_PAY)."},
                    "txn_type": {"type": "string", "description": "Transaction type (e.g., 'UPI_COLLECT', 'UPI_PAY')."},
                    "is_emi": {"type": "string", "description": "Whether this is an EMI payment."},
                    "emi_bank": {"type": "string", "description": "Bank offering EMI."},
                    "emi_tenure": {"type": "string", "description": "EMI tenure in months."}
                }
            }
        },
        "customer": {
            "type": "object",
            "properties": {
                "id": {"type": "string", "description": "Customer identifier."},
                "email": {"type": "string", "description": "Customer email address."},
                "mobile": {"type": "string", "description": "Customer mobile number."}
            }
        },
        "offer_code": {
            "type": "string",
            "description": "Coupon or offer code to apply."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}

juspay_offer_order_status_schema = {
    "type": "object",
    "required": ["order_id"],
    "properties": {
        "order_id": {
            "type": "string",
            "description": "Unique identifier for the order to check status with offer details."
        },
        "routing_id": {
            "type": "string",
            "description": "Optional custom routing ID for the API request."
        }
    }
}