import * as React from "react";
import styles from "./Header.module.css";

export default function Header() {
  return (
    <div>
      <h3 className={styles.headerTitle}>
        This is going to be the header component{" "}
      </h3>
    </div>
  );
}
