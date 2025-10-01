function autoFill(obj, name = "env", cfg = {}) {
  /* ============ 1. 配置合并 ============ */
  const config = {
    depth: 0, // 内部用，勿传
    maxDepth: 1, // 递归深度；-1 无限
    fillMissing: false, // 缺失时自动补 {}
    warnMissing: true, // 缺失时打印警告
    logGet: true, // 打印 GET
    logSet: false, // 打印 SET
    logHas: false, // 打印 HAS
    logDelete: false, // 打印 DELETE
    logCall: false, // 打印函数调用
    logConstruct: false, // 打印 new
    logCallArgs: true, // 打印函数参数
    logCallResult: false, // 打印函数返回值
    blackList: [], // 命中后不再递归
    whiteList: [], // 只打印白名单 key；[] = 全部
    ...cfg,
  };

  /* ============ 2. 工具 ============ */
  const isPrimitive = (v) =>
    v == null || (typeof v !== "object" && typeof v !== "function");
  const isBuiltinSymbol = (k) => typeof k === "symbol";
  const shouldLog = (key) => {
    if (config.whiteList.length) return config.whiteList.includes(String(key));
    const ignore = ["__proto__", "constructor"];
    return !ignore.includes(String(key));
  };

  if (isPrimitive(obj)) return obj;
  if (config.blackList.includes(name)) return obj;

  /* ============ 3. 主代理 ============ */
  return new Proxy(obj, {
    get(target, key, receiver) {
      if (isBuiltinSymbol(key)) return Reflect.get(target, key, receiver);

      let value = Reflect.get(target, key, receiver);

      /* 缺失报警 / 自动补 */
      if (value === undefined && config.warnMissing) {
        console.warn(`🚨 缺失属性: ${name}.${String(key)}`);
        if (config.fillMissing) {
          value = {};
          target[key] = value;
        }
      }

      /* 日志 */
      if (config.logGet && shouldLog(key)) {
        console.log(`[GET] ${name},     属性:${String(key)},    值: ${value}`);
      }

      /* 函数代理 */
      if (typeof value === "function") {
        return new Proxy(value, {
          apply(fn, thisArg, argList) {
            if (config.logCall && shouldLog(key)) {
              console.log(`[CALL] ${name}.${String(key)}`);
              if (config.logCallArgs) console.log(`  └─ args:`, argList);
            }
            const ret = Reflect.apply(fn, thisArg, argList);
            if (config.logCallResult && shouldLog(key))
              console.log(`  └─ ret:`, ret);
            return ret;
          },
          construct(fn, argList) {
            if (config.logConstruct && shouldLog(key)) {
              console.log(`[NEW] ${name}.${String(key)}`);
              if (config.logCallArgs) console.log(`  └─ args:`, argList);
            }
            return Reflect.construct(fn, argList);
          },
        });
      }

      /* 下一层代理 */
      return config.maxDepth < 0 || config.depth < config.maxDepth
        ? autoFill(value, `${name}.${String(key)}`, {
            ...config,
            depth: config.depth + 1,
          })
        : value;
    },

    set(target, key, val, receiver) {
      if (config.logSet && shouldLog(key))
        console.log(`[SET] ${name}.${String(key)} =`, val);
      return Reflect.set(target, key, val, receiver);
    },

    has(target, key) {
      if (config.logHas && shouldLog(key))
        console.log(`[HAS] ${String(key)} in ${name}`);
      return key in target;
    },

    deleteProperty(target, key) {
      if (config.logDelete && shouldLog(key))
        console.log(`[DELETE] ${name}.${String(key)}`);
      return delete target[key];
    },
  });
}


var window = autoFill(
  {
    outerWidth:123,
    screen:autoFill({
      width:1920,
      height:768,
      "0":""
    },"screen")
  },
  "window"
);

let document = autoFill(
  {
    body:autoFill({
      scrollHeight:1000,
      scrollWidth:1000,
    },"body")
  },"document"
)
window.document = document
console.log('[ window.document.scrollHeight ] >',window.document.body.scrollHeight )