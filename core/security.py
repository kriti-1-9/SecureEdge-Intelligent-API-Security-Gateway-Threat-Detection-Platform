
def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise ValueError("Token is missing subject")

        return payload

    except jwt.InvalidTokenError as exc:
        raise ValueError("Invalid or expired access token") from exc
