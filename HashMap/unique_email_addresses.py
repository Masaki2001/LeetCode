class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        checked = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            checked.add(local.replace('.', '') + '@' + domain)

        return len(checked)