    # full support for alter table is not available in SQLite, so we'll simulate it
    # for table, fks in foreign_keys.items():
    #     print(table)
    #     print(fks)
    #     alter_query = f"ALTER TABLE {table}\n"
    #     for fk in fks:
    #         if fk == fks[-1]:
    #             alter_query += f"ADD CONSTRAINT fk_{table}_{fk[0]} FOREIGN KEY ({fk[0]}) REFERENCES {fk[1]}({fk[2]});\n"
    #         else:
    #             alter_query += f"ADD CONSTRAINT fk_{table}_{fk[0]} FOREIGN KEY ({fk[0]}) REFERENCES {fk[1]}({fk[2]}),\n"
    #     cursor.execute(alter_query)