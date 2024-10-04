

export function checkPassword(password){

    if (typeof password !== 'string') {
        return false
    }

    if (password.length < 8) {
        return false
    }

    if (password.length > 20) {
        return false
    }

    if (!/[A-Z]/.test(password)) {
        return false
    }

    if (!/[a-z]/.test(password)) {
        return false
    }

    if (!/\d/.test(password)) {
        return false
    }

    if (!/[^A-Za-z0-9]/.test(password)) {
        return false
    }

    return true
}

export function checkPasswordAndThrowReason(password){

    if (typeof password !== 'string') {
        throw new Error('Password must be a string')
    }

    if (password.length < 8) {
        throw new Error('Password must be at least 8 characters long')
    }

    if (password.length > 20) {
        throw new Error('Password must be at most 20 characters long')
    }

    if (!/[A-Z]/.test(password)) {
        throw new Error('Password must contain at least one uppercase letter')
    }

    if (!/[a-z]/.test(password)) {
        throw new Error('Password must contain at least one lowercase letter')
    }

    if (!/\d/.test(password)) {
        throw new Error('Password must contain at least one digit')
    }

    // passwords can't contain the ! character:
    if (/!/.test(password)) {
        throw new Error('Password cannot contain the ! character')
    }

    if (!/[^A-Za-z0-9]/.test(password)) {
        throw new Error('Password must contain at least one special character')
    }

    return true
}