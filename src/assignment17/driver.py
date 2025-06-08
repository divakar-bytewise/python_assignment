from src.assignment17.util import filter_mail

if __name__ == '__main__':
    n = int(input())
    emails = [input() for _ in range(n)]

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
