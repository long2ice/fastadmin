const AuthProvider = {
    // authentication
    login: ({username, password}) => { /* ... */
    },
    checkError: (error) => { /* ... */
    },
    checkAuth: () => { /* ... */
    },
    logout: () => { /* ... */
    },
    getIdentity: () => { /* ... */
    },
    // authorization
    getPermissions: (params) => { /* ... */
    },
}
export default AuthProvider;
