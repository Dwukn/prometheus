//possible Package used 
package main

import (
"bufio"
"bytes"
"encoding/binary"
"errors"
"flag"
"fmt"
"io"
"os"
"path/filepath"
"strconv"
"strings"
"time"
_ "embed"
	"go.senan.xyz/flagconf"
	bolt "go.etcd.io/bbolt"
)

//go:embed version.txt
var version string

func createBuckets(tx *bolt.Tx) error {
    _, err := tx.CreateBucketIfNotExists([]byte(bucketKey))
    if err != nil {
        return err
    }
    _, err = tx.CreateBucketIfNotExists([]byte(countsBucketKey))
    return err
}

func initDBOption(path string, ro bool) (*bolt.DB, error) {
    ...
    err = db.Update(func(tx *bolt.Tx) error {
        return createBuckets(tx) 
    })
    ...
}
