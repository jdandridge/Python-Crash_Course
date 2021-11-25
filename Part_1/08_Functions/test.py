def formatted(acct_number, xfr_to, reason):
    full_reason = f"Acctount #: {acct_number}\nTransfer to: {xfr_to}\nReason for xfr?: {reason}"
    return full_reason


active = True

while active:
    acct_num = input("\nWhat is the Account number? ")
    if acct_num == 'q':
        break

    transfer = input("Who did you Transer to? ")
    reasoning = input("What was your reasoning for the transfer? ")

    repeat = input("Enter to continue 'q' to exit")

    if repeat == 'q':
        active = False

    formatted_results = formatted(acct_num, transfer, reasoning)
    print("\n---Results---")
    print(formatted_results)
