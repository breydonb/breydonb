import React, {createContext, useContext, useEffect, useState} from 'react'
import {createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, onAuthStateChanged, updateProfile } from 'firebase/auth'
import { auth } from "../index";

const UserContext = createContext();

export const AuthContextProvider = ({children}) => {
    const[user, setUser] = useState({});
    const createUser = (email, password) => {
        return createUserWithEmailAndPassword(auth, email, password)
    }

    const logout = () => {
        return signOut(auth)
    }

    const signin = (email, password) => {
        return signInWithEmailAndPassword(auth, email, password)
    }

    const updateUserProfile = async (displayName, photoURL) => {
        updateProfile(auth.currentUser, {
            displayName: displayName, photoURL: photoURL
          }).then(() => {
            // Profile updated!
            // ...
          }).catch((error) => {
            // An error occurred
            // ...
          });
    }

    useEffect(() =>{
        const unsubscribe = onAuthStateChanged(auth, (currentUser) =>{
          console.log(currentUser);
          setUser(currentUser);
        })
        return () => {
            unsubscribe();
        }
    },[])

    return(
        <UserContext.Provider value={{createUser, user, logout, signin, updateUserProfile}}>
            {children}
        </UserContext.Provider>
    )
}

export const UserAuth = () =>{
    return useContext(UserContext)
}
