import React from 'react'
import { UserAuth } from '../contexts/AuthContext'

function Account() {
    const {user} = UserAuth();
    return (
        <div>{user.email}</div>
    )
}

export default Account