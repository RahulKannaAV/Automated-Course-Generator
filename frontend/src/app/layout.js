import { Inter } from "next/font/google";
import "./globals.css";
import { AppRouterCacheProvider } from '@mui/material-nextjs/v15-appRouter';

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Automated Course Generator",
  description: "Next JS app to make learning easier",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
        <head>
          <link rel="preconnect" href="https://fonts.googleapis.com" />
          <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="true" />
          <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet" />
        </head>
        <body className={inter.className}>
          <AppRouterCacheProvider>
            {children}
            </AppRouterCacheProvider>
        </body>
    </html>
  );
}
