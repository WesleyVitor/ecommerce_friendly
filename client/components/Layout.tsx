import React, {FC} from 'react'


import { Header } from './Header';

interface LayoutProps {
    children: React.ReactNode
}


const Layout: FC<LayoutProps> = (props:LayoutProps)=>{
    return (
        <div>
            <Header/>
            <main className='container d-flex justify-content-center mt-5'>
                {props.children}
            </main>
        </div>
    )
}

export default Layout;
