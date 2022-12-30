class CredentialVerifier:
    @staticmethod
    def is_username_available(username: str | None) -> bool:
        if username:
            return False
        return True

    @staticmethod
    def is_email_available(email: str | None) -> bool:
        if email:
            return False
        return True


def get_credential_verifier() -> CredentialVerifier:
    return CredentialVerifier()


credential_verifier: CredentialVerifier = get_credential_verifier()
