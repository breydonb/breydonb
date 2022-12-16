import React, {createContext, useContext, useEffect, useState} from 'react'
import { db } from "../index";
import { collection, getDocs, setDoc, getDoc, doc } from 'firebase/firestore';

const FirestoreContext = createContext();

export const FirestoreContextProvider = ({children}) => {
    const[displayName, setDisplayName] = useState('');
    const[photoURL, setPhotoUrl] = useState('');

    const createUserInformation = async (fullName, hasAdminPrivilege, imageUrl, username, uid) => {
        try {
            const docRef = await setDoc(doc(db, "users", uid), {
              displayName: fullName,
              hasAdmin: hasAdminPrivilege,
              imageUrl: imageUrl,
              userName: username,
              uid: uid
            });
            console.log("Document written with ID: ", docRef.id);
          } 
        catch (e) {
            console.error("Error adding document: ", e);
          }
    }

    // Gets all users
    const getAllUserInformation = async () => {
      const querySnapshot = await getDocs(collection(db, "users"));
      querySnapshot.forEach((doc) => {
        console.log(`${doc.id} => ${doc.data()}`);
      });
    }

    // Gets one user's info from document
    const getUserInformation = async (uid) => {
      const docRef = doc(db, "users", uid);
      const docSnap = await getDoc(docRef);
      if (docSnap.exists()) {
        // console.log("Document data:", docSnap.data());
        setDisplayName(docSnap.data().displayName);
        setPhotoUrl(docSnap.data().imageUrl);

        
      } else {
          // doc.data() will be undefined in this case
          console.log("No such document!");
      }
    }

    return(
        <FirestoreContext.Provider value={ {createUserInformation, getAllUserInformation, getUserInformation, displayName}}>
            {children}
        </FirestoreContext.Provider>
    )
}

export const FirestoreQueryContext = () =>{
    return useContext(FirestoreContext);
}